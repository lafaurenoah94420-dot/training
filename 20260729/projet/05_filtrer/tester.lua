-- Tester — Filtrer les gros

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


if type(main.filtrer_gros) ~= "function" then
  print("❌ Erreur : la fonction filtrer_gros n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function filtrer_gros(...)")
  os.exit(1)
end

local r = main.filtrer_gros({2, 8, 3, 12, 5})
_tester("#résultat == 2", #r, 2)
_tester("r[1] == 8", r[1], 8)
_tester("r[2] == 12", r[2], 12)
local r2 = main.filtrer_gros({1, 2, 3})
_tester("aucun gros → # == 0", #r2, 0)
local r3 = main.filtrer_gros({10, 6})
_tester("r3[1] == 10", r3[1], 10)

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

