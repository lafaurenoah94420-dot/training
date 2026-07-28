-- ============================================================
-- Exercice 1/6 — Lire un journal
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260728/projet/01_lire
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260728/projet/01_lire/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
f = io.open("journal.txt", "r")
contenu = f:read("*a")
f:close()