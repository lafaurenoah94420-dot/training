-- ============================================================
-- Tester — Deux fonctions
-- ============================================================

local function load_main()
  local env = setmetatable({}, { __index = _G })
  local chunk, err = loadfile("main.lua", "t", env)
  if not chunk then
    print("❌ Erreur de chargement : " .. tostring(err))
    print("   → Vérifie que main.lua existe et n'a pas d'erreur de syntaxe")
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


if type(main.degats) ~= "function" then
  print("❌ Erreur : la fonction degats n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function degats(...)")
  os.exit(1)
end
if type(main.est_vivant) ~= "function" then
  print("❌ Erreur : la fonction est_vivant n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function est_vivant(...)")
  os.exit(1)
end

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

-- ---- Tests ----

_tester("degats(50, 20) → 30", main.degats(50, 20), 30)
_tester("degats(10, 40) → 0", main.degats(10, 40), 0)
_tester("degats(0, 5) → 0", main.degats(0, 5), 0)
_tester("est_vivant(30) → true", main.est_vivant(30), true)
_tester("est_vivant(0) → false", main.est_vivant(0), false)

-- ---- Résultat ----
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
