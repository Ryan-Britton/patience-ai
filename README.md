# Patience‑AI – Simplified Root Stack

**Compose file and Dockerfile are now at repo root** to avoid path confusion on Windows/Linux.

## Quick start (Windows PowerShell or bash)

```powershell
git clone <your‑fork>
cd patience-ai
Copy-Item .env.example .env      # add your keys
docker compose up -d --build
```

Then open:
* LangServe root: http://localhost:8000/
* Chat UI:        http://localhost:8000/chat
* n8n:            http://localhost:5678

Hot‑reload works out‑of‑the‑box; edit any file under `apps\email_manager\`.
