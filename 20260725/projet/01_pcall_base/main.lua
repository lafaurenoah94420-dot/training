-- ============================================================
-- Exercice 1/6 — Essayer sans planter
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260725/projet/01_pcall_base
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260725/projet/01_pcall_base/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
ok_soin, resultat_soin = pcall(function ()
    return 40 + 25
end)

ok_porte, message_porte= pcall(function ()
    return error("porte verrouillee")
end)