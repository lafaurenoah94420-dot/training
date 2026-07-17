-- ============================================================
-- Tester — Kit de survie
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


if type(main.soigner) ~= "function" then
  print("❌ Erreur : la fonction soigner n'est pas définie dans main.lua")
  os.exit(1)
end
if type(main.degats) ~= "function" then
  print("❌ Erreur : la fonction degats n'est pas définie dans main.lua")
  os.exit(1)
end
if type(main.statut) ~= "function" then
  print("❌ Erreur : la fonction statut n'est pas définie dans main.lua")
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

_tester("soigner(70, 40) → 100", main.soigner(70, 40), 100)
_tester("soigner(40, 10) → 50", main.soigner(40, 10), 50)
_tester("degats(25, 30) → 0", main.degats(25, 30), 0)
_tester("degats(80, 15) → 65", main.degats(80, 15), 65)
_tester('statut(20) → "Critique"', main.statut(20), "Critique")
_tester('statut(45) → "Blessé"', main.statut(45), "Blessé")
_tester('statut(80) → "Stable"', main.statut(80), "Stable")

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
