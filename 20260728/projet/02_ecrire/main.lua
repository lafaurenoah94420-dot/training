-- ============================================================
-- Exercice 2/6 — Écrire une sauvegarde
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260728/projet/02_ecrire
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260728/projet/02_ecrire/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
f = io.open("sauvegarde.txt", "w")

f:write("vie=80")

f:close()