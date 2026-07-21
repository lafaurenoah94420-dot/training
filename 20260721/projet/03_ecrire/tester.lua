-- ============================================================
-- Tester — Écrire une clé
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

if type(main.blesser) ~= "function" then
  print("❌ Erreur : la fonction blesser n'est pas définie dans main.lua")
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


local p = { nom = "Leon", vie = 80 }
main.blesser(p, 25)
_tester("après blesser 25, vie == 55", p.vie, 55)
main.blesser(p, 10)
_tester("après encore 10, vie == 45", p.vie, 45)
local q = { vie = 5 }
main.blesser(q, 5)
_tester("vie peut aller à 0", q.vie, 0)


local _passes = 0
for _, r in ipairs(_resultats) do if r then _passes = _passes + 1 end end
local _total = #_resultats
print("\n" .. string.rep("─", 40))
print(string.format("  %d/%d tests passés", _passes, _total))
if _passes == _total then print("  🎉 Parfait !")
else print(string.format("  %d test(s) à corriger.", _total - _passes)) end
print(string.rep("─", 40))
