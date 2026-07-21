-- ============================================================
-- Tester — Parcourir avec pairs
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

if type(main.somme_valeurs) ~= "function" then
  print("❌ Erreur : la fonction somme_valeurs n'est pas définie dans main.lua")
  os.exit(1)
end

if type(main.nombre_cles) ~= "function" then
  print("❌ Erreur : la fonction nombre_cles n'est pas définie dans main.lua")
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


_tester("somme_valeurs({a=10,b=20}) → 30", main.somme_valeurs({a=10,b=20}), 30)
_tester("somme_valeurs({x=5}) → 5", main.somme_valeurs({x=5}), 5)
_tester("somme_valeurs({}) → 0", main.somme_valeurs({}), 0)
_tester("nombre_cles({a=1,b=2,c=3}) → 3", main.nombre_cles({a=1,b=2,c=3}), 3)
_tester("nombre_cles({}) → 0", main.nombre_cles({}), 0)


local _passes = 0
for _, r in ipairs(_resultats) do if r then _passes = _passes + 1 end end
local _total = #_resultats
print("\n" .. string.rep("─", 40))
print(string.format("  %d/%d tests passés", _passes, _total))
if _passes == _total then print("  🎉 Parfait !")
else print(string.format("  %d test(s) à corriger.", _total - _passes)) end
print(string.rep("─", 40))
