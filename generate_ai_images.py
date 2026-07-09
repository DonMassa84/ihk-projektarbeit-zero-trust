#!/usr/bin/env python3
"""
Generiere KI-Architektur-Bilder für die IHK-Projektdokumentation
Nutzt Flux.1-dev (via diffusers) oder SDXL - optimiert für RTX 3060 12GB
"""

import os
import torch
from diffusers import FluxPipeline, StableDiffusionXLPipeline
from diffusers.utils import load_image
import gc

# Ausgabe-Verzeichnis
OUT_DIR = "/home/schattenmacher/openclaw-workspace/ihk_zero_trust_projektarbeit_final/10_screenshots/ai_generated"
os.makedirs(OUT_DIR, exist_ok=True)

# Prompts aus architecture_prompts.md
PROMPTS = {
    "01_zerotrust_architecture": {
        "prompt": "Professional technical architecture diagram, Zero Trust security model, layered architecture: Presentation Layer (React Self-Service Portal), Application Layer (Node.js Business Logic, Policy Engine, Workflow Engine), Data Layer (PostgreSQL with Audit Logs, Redis Cache), Integration Layer (GitHub API, Azure AD/SAML, REST APIs). Clean lines, modern corporate style, blue/gray color scheme, labeled components, arrows showing data flow, high resolution, technical documentation quality, isometric view.",
        "negative": "messy, hand-drawn, low quality, blurry, watermark, text artifacts, cartoon, bright colors, unprofessional",
        "filename": "architecture_zerotrust.png"
    },
    "02_github_workflow": {
        "prompt": "Flowchart of GitHub Actions CI/CD pipeline for automated role provisioning: Trigger (Issue labeled role-request) -> Validate Stage (Policy Check, Required Fields) -> Approve Stage (Manager Approval, 48h Escalation) -> Provision Stage (GitHub API Team Assignment, Repository Permissions) -> Notify Stage (Email/Slack, Audit Log Entry). Modern DevOps diagram style, GitHub brand colors (purple/black/white), clear step boxes, decision diamonds, success/failure paths, professional technical illustration.",
        "negative": "cluttered, confusing arrows, low contrast, unreadable text, amateur",
        "filename": "github_workflow.png"
    },
    "03_rbac_model": {
        "prompt": "Entity Relationship Diagram for Role-Based Access Control: User (1) -> has -> (*) Role, Role (*) -> contains -> (*) Permission, Role (1) -> maps_to -> (1) GitHubTeam, GitHubTeam (*) -> grants_access -> (*) Repository. Clean ERD notation (Crow's Foot), professional database diagram style, white background, blue entities, black relationships, clear cardinality markers, high quality technical documentation.",
        "negative": "hand-drawn, fuzzy, incorrect notation, messy layout, colors bleeding",
        "filename": "rbac_model.png"
    },
    "04_selfservice_process": {
        "prompt": "Business process diagram (BPMN-style) for Self-Service Role Request: Employee logs in via SSO -> Selects Role from Catalog -> Policy Engine validates -> Manager receives Approval Request -> Manager Approves/Rejects -> If Approved: GitHub API provisions access -> Audit Log records transaction -> Employee notified. Swimlanes for Employee, Manager, System, GitHub. Professional BPMN notation, corporate blue/gray, clean lanes, clear start/end events.",
        "negative": "non-standard notation, messy swimlanes, unclear flow, amateur drawing",
        "filename": "selfservice_process.png"
    },
    "05_audit_anomaly": {
        "prompt": "Security monitoring architecture: Audit Logs (Append-Only PostgreSQL) -> Stream Processing -> ML Anomaly Detector (CodeBERT Embedding) -> Anomaly Score -> Threshold Check -> Alert Generation -> Security Team Dashboard. Data flow diagram, modern SOC style, dark theme with accent colors (red for alerts, green for normal), clear component boundaries, technical precision.",
        "negative": "bright colors, cartoon, unclear components, messy data flows",
        "filename": "audit_anomaly.png"
    },
    "06_deployment_architecture": {
        "prompt": "Cloud-native deployment diagram: GitHub Repository -> GitHub Actions CI/CD -> Docker Images -> Kubernetes Cluster (Ingress, Self-Service Pods, Backend Pods, PostgreSQL StatefulSet, Redis) -> Monitoring (Prometheus/Grafana) -> GitHub Audit Log Integration. Kubernetes official style icons, clean clusters, labeled namespaces, professional infrastructure diagram.",
        "negative": "messy, incorrect k8s icons, cluttered, low resolution",
        "filename": "deployment_architecture.png"
    }
}

def generate_with_flux():
    """Flux.1-dev via diffusers (benötigt ~12GB VRAM mit offloading)"""
    print("Lade Flux.1-dev Pipeline...")
    pipe = FluxPipeline.from_pretrained(
        "black-forest-labs/FLUX.1-dev",
        torch_dtype=torch.bfloat16,
        device_map="balanced",
        low_cpu_mem_usage=True
    )
    pipe.enable_model_cpu_offload()
    pipe.enable_vae_slicing()
    return pipe

def generate_with_sdxl():
    """SDXL als Fallback (weniger VRAM)"""
    print("Lade SDXL Pipeline...")
    pipe = StableDiffusionXLPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float16,
        variant="fp16",
        use_safetensors=True
    )
    pipe.enable_model_cpu_offload()
    pipe.enable_vae_slicing()
    return pipe

def generate_images(pipe, model_name="flux"):
    """Generiere alle 6 Bilder"""
    for key, config in PROMPTS.items():
        print(f"\n{'='*60}")
        print(f"Generiere: {config['filename']}")
        print(f"{'='*60}")
        
        out_path = os.path.join(OUT_DIR, config['filename'])
        
        if os.path.exists(out_path):
            print(f"  ⏭  Überspringe (existiert bereits)")
            continue
        
        try:
            if model_name == "flux":
                image = pipe(
                    prompt=config["prompt"],
                    negative_prompt=config["negative"],
                    width=1024,
                    height=768,
                    num_inference_steps=20,
                    guidance_scale=3.5,
                    generator=torch.Generator(device="cuda").manual_seed(42)
                ).images[0]
            else:  # SDXL
                image = pipe(
                    prompt=config["prompt"],
                    negative_prompt=config["negative"],
                    width=1024,
                    height=768,
                    num_inference_steps=25,
                    guidance_scale=7.5,
                    generator=torch.Generator(device="cuda").manual_seed(42)
                ).images[0]
            
            image.save(out_path)
            print(f"  ✅ Gespeichert: {out_path}")
            
            # VRAM freigeben
            gc.collect()
            torch.cuda.empty_cache()
            
        except Exception as e:
            print(f"  ❌ Fehler: {e}")

if __name__ == "__main__":
    print(f"CUDA verfügbar: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
    
    # Erst Flux versuchen, bei OOM auf SDXL fallen
    try:
        pipe = generate_with_flux()
        generate_images(pipe, "flux")
    except torch.cuda.OutOfMemoryError:
        print("\n⚠️  Flux OOM -> falle auf SDXL zurück")
        gc.collect()
        torch.cuda.empty_cache()
        pipe = generate_with_sdxl()
        generate_images(pipe, "sdxl")
    except Exception as e:
        print(f"\n❌ Flux Fehler: {e}")
        print("Versuche SDXL...")
        gc.collect()
        torch.cuda.empty_cache()
        pipe = generate_with_sdxl()
        generate_images(pipe, "sdxl")
    
    print(f"\n🎉 Fertig! Bilder in: {OUT_DIR}")