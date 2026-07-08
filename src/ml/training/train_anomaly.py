import json, os, sys, numpy as np
from datasets import Dataset
from transformers import (
    AutoTokenizer, AutoModelForSequenceClassification,
    TrainingArguments, Trainer, EarlyStoppingCallback,
)
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

MODEL_NAME = "microsoft/codebert-base"
OUTPUT_DIR = os.path.expanduser("~/.cache/zt-models/anomaly-detector")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open("audit_dataset.json") as f:
    data = json.load(f)

texts = [d["text"] for d in data]
labels = [d["label"] for d in data]
print(f"Dataset: {len(texts)} samples, {sum(labels)} anomalies ({sum(labels)/len(labels)*100:.1f}%)")

train_texts = texts[:1600]; train_labels = labels[:1600]
eval_texts = texts[1600:]; eval_labels = labels[1600:]

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

def tokenize(batch):
    return tokenizer(batch["text"], padding="max_length", truncation=True, max_length=128)

train_ds = Dataset.from_dict({"text": train_texts, "label": train_labels}).map(tokenize, batched=True)
eval_ds = Dataset.from_dict({"text": eval_texts, "label": eval_labels}).map(tokenize, batched=True)

def compute_metrics(pred):
    logits, truths = pred
    preds = np.argmax(logits, axis=1)
    precision, recall, f1, _ = precision_recall_fscore_support(truths, preds, average="binary")
    acc = accuracy_score(truths, preds)
    return {"accuracy": acc, "f1": f1, "precision": precision, "recall": recall}

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=32,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="f1",
    logging_dir=f"{OUTPUT_DIR}/logs",
    logging_steps=10,
    report_to="none",
    fp16=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=eval_ds,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2)],
)

trainer.train()
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print(f"\n✅ Modell gespeichert in {OUTPUT_DIR}")

metrics = trainer.evaluate()
print(f"\n📊 Eval-Metriken:")
for k, v in metrics.items():
    print(f"   {k}: {v:.4f}")
