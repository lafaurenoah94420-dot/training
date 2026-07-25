-- ============================================================
-- Tester — Kit manoir
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


if type(main.verrou) ~= "function" then
  print("❌ Erreur : la fonction verrou n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function verrou(...)")
  os.exit(1)
end


if type(main.entrer) ~= "function" then
  print("❌ Erreur : la fonction entrer n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function entrer(...)")
  os.exit(1)
end


if type(main.dose) ~= "function" then
  print("❌ Erreur : la fonction dose n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function dose(...)")
  os.exit(1)
end

_tester("verrou(314) → true", main.verrou(314), true)
local ok_bad, _ = pcall(main.verrou, 100)
_tester("verrou(100) échoue", ok_bad, false)
_tester('entrer(314) → "entree"', main.entrer(314), "entree")
_tester('entrer(100) → "bloque"', main.entrer(100), "bloque")
_tester("dose(80, 30) → 50", main.dose(80, 30), 50)
_tester("dose(20, 50) → 0", main.dose(20, 50), 0)
local ok_dose, _ = pcall(main.dose, 50, 0)
_tester("dose(50, 0) échoue", ok_dose, false)

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

