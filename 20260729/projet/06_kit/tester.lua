-- Tester — Kit inventaire

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


if type(main.creer) ~= "function" then
  print("❌ Erreur : la fonction creer n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function creer(...)")
  os.exit(1)
end


if type(main.ajouter) ~= "function" then
  print("❌ Erreur : la fonction ajouter n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function ajouter(...)")
  os.exit(1)
end


if type(main.compter) ~= "function" then
  print("❌ Erreur : la fonction compter n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function compter(...)")
  os.exit(1)
end


if type(main.contient) ~= "function" then
  print("❌ Erreur : la fonction contient n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function contient(...)")
  os.exit(1)
end

local inv = main.creer()
_tester("#creer() == 0", #inv, 0)
main.ajouter(inv, "herb")
main.ajouter(inv, "ammo")
main.ajouter(inv, "herb")
_tester("compter herb → 2", main.compter(inv, "herb"), 2)
_tester("compter ammo → 1", main.compter(inv, "ammo"), 1)
_tester("compter clé → 0", main.compter(inv, "clé"), 0)
_tester('contient "ammo" → true', main.contient(inv, "ammo"), true)
_tester('contient "clé" → false', main.contient(inv, "clé"), false)

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

