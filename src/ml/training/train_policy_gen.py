import os, random, torch
from transformers import (
    AutoTokenizer, AutoModelForSeq2SeqLM,
    Trainer, TrainingArguments,
)

MODEL_NAME = "google/flan-t5-small"
OUTPUT_DIR = os.path.expanduser("~/.cache/zt-models/policy-generator")
os.makedirs(OUTPUT_DIR, exist_ok=True)

policy_data = [
    ("policy: admin full access", "ALLOW: admin/* * FOR role=Admin"),
    ("policy: developer write frontend", "ALLOW: frontend/* WRITE FOR role=Developer"),
    ("policy: auditor read logs", "ALLOW: audit/* READ FOR role=Auditor"),
    ("policy: intern read docs", "ALLOW: docs/* READ FOR role=Intern"),
    ("policy: viewer read only", "ALLOW: * READ FOR role=Viewer"),
    ("policy: guest view public", "ALLOW: public/* READ FOR role=Guest"),
    ("policy: finance read billing", "ALLOW: finance/billing READ FOR role=Finance"),
    ("policy: hr write personnel", "ALLOW: hr/* WRITE FOR role=HR"),
    ("policy: devops deploy staging", "ALLOW: deploy/staging * FOR role=DevOps"),
    ("policy: security read audit", "ALLOW: audit/* READ FOR role=Security"),
    ("policy: qa write test", "ALLOW: test/* WRITE FOR role=QA"),
    ("policy: contractor limited", "ALLOW: contractor/* READ FOR role=Contractor"),
    ("policy: analyst dashboards", "ALLOW: dashboards/* READ FOR role=Analyst"),
    ("policy: block terminated", "DENY: * * FOR role=Terminated"),
    ("policy: support tickets", "ALLOW: support/tickets WRITE FOR role=Support"),
    ("policy: admin manage roles", "ALLOW: roles/* * FOR role=Admin"),
    ("policy: devops infra", "ALLOW: infra/* WRITE FOR role=DevOps"),
    ("policy: security incidents", "ALLOW: incidents/* WRITE FOR role=Security"),
    ("policy: partner shared", "ALLOW: shared/* READ FOR role=Partner"),
    ("policy: datascientist ml", "ALLOW: data/ml READ FOR role=Data-Scientist"),
]

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

input_ids_list, label_ids_list = [], []
for inp, out in policy_data:
    tokens = tokenizer(inp, padding="max_length", truncation=True, max_length=32, return_tensors="pt")
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(out, padding="max_length", truncation=True, max_length=32, return_tensors="pt")
    input_ids_list.append(tokens["input_ids"][0])
    label_ids_list.append(labels["input_ids"][0])

class PolicyDataset(torch.utils.data.Dataset):
    def __init__(self, input_ids, labels):
        self.input_ids = input_ids
        self.labels = labels
    def __len__(self):
        return len(self.input_ids)
    def __getitem__(self, i):
        return {"input_ids": self.input_ids[i], "labels": self.labels[i], "attention_mask": torch.ones_like(self.input_ids[i])}

random.seed(42)
indices = list(range(len(policy_data)))
random.shuffle(indices)
split = int(len(indices) * 0.8)
train_idx, eval_idx = indices[:split], indices[split:]

train_ds = PolicyDataset([input_ids_list[i] for i in train_idx], [label_ids_list[i] for i in train_idx])
eval_ds = PolicyDataset([input_ids_list[i] for i in eval_idx], [label_ids_list[i] for i in eval_idx])

args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=80,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    eval_strategy="epoch",
    save_strategy="no",
    logging_steps=5,
    report_to="none",
    fp16=True,
    remove_unused_columns=False,
    prediction_loss_only=True,
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_ds,
    eval_dataset=eval_ds,
    tokenizer=tokenizer,
)

trainer.train()
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print(f"\nModel saved to {OUTPUT_DIR}")
print("\nTest - run inference with: python3 -c \"from transformers import AutoModelForSeq2SeqLM, AutoTokenizer; import torch; m = AutoModelForSeq2SeqLM.from_pretrained('" + OUTPUT_DIR + "').to('cuda'); t = AutoTokenizer.from_pretrained('" + OUTPUT_DIR + "'); i = t('policy: developer write frontend', return_tensors='pt').to('cuda'); o = m.generate(**i, max_new_tokens=32); print(t.decode(o[0], skip_special_tokens=True))\"")
