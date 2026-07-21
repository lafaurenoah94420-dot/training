-- ============================================================
-- Tester — Fonction qui lit
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

if type(main.get_vie) ~= "function" then
  print("❌ Erreur : la fonction get_vie n'est pas définie dans main.lua")
  os.exit(1)
end

if type(main.get_nom) ~= "function" then
  print("❌ Erreur : la fonction get_nom n'est pas définie dans main.lua")
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


local p = { nom = "Joel", vie = 60 }
_tester('get_vie(p) → 60', main.get_vie(p), 60)
_tester('get_nom(p) → "Joel"', main.get_nom(p), "Joel")
_tester('get_vie({vie=0}) → 0', main.get_vie({vie=0}), 0)


local _passes = 0
for _, r in ipairs(_resultats) do if r then _passes = _passes + 1 end end
local _total = #_resultats
print("\n" .. string.rep("─", 40))
print(string.format("  %d/%d tests passés", _passes, _total))
if _passes == _total then print("  🎉 Parfait !")
else print(string.format("  %d test(s) à corriger.", _total - _passes)) end
print(string.rep("─", 40))
