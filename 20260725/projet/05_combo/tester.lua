-- ============================================================
-- Tester — Tenter un soin en sécurité
-- ============================================================

local function load_main()
  local env = setmetatable({}, { __index = _G })
  local chunk, err = loadfile("main.lua", "t", env)
  if not chunk then
    print("❌ Erreur de chargement : " .. tostring(err))
    os.exit(1)
  end
  local ok, err2 = pcall(chunk)
  if not ok then
    print("❌ Erreur d'exécution dans main.lua : " .. tostring(err2))
    os.exit(1)
  end
  return env
end

local main = load_main()

local _resultats = {}

local function _tester(description, obtenu, attendu)
  if obtenu == attendu then
    print("✅ " .. description)
    table.insert(_resultats, true)
  else
    print("❌ " .. description)
    print("   Attendu : " .. tostring(attendu))
    print("   Obtenu  : " .. tostring(obtenu))
    table.insert(_resultats, false)
  end
end


if type(main.appliquer_soin) ~= "function" then
  print("❌ Erreur : la fonction appliquer_soin n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function appliquer_soin(...)")
  os.exit(1)
end


if type(main.soin_sur) ~= "function" then
  print("❌ Erreur : la fonction soin_sur n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function soin_sur(...)")
  os.exit(1)
end

_tester("appliquer_soin(40, 30) → 70", main.appliquer_soin(40, 30), 70)
local ok, _ = pcall(main.appliquer_soin, 40, -5)
_tester("appliquer_soin(40, -5) échoue", ok, false)
_tester("soin_sur(40, 30) → 70", main.soin_sur(40, 30), 70)
_tester("soin_sur(40, -5) → 40 (vie inchangée)", main.soin_sur(40, -5), 40)
_tester("soin_sur(90, 10) → 100", main.soin_sur(90, 10), 100)

local _passes = 0
for _, r in ipairs(_resultats) do if r then _passes = _passes + 1 end end
local _total = #_resultats
print("\n" .. string.rep("─", 40))
print(string.format("  %d/%d tests passés", _passes, _total))
if _passes == _total then
  print("  🎉 Parfait !")
else
  print(string.format("  %d test(s) à corriger.", _total - _passes))
end
print(string.rep("─", 40))

