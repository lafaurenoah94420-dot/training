-- ============================================================
-- Tester — Fonction pour lire
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


if type(main.lire) ~= "function" then
  print("❌ Erreur : la fonction lire n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function lire(...)")
  os.exit(1)
end


local f = io.open("_tmp_a.txt", "w"); f:write("herb"); f:close()
local f2 = io.open("_tmp_b.txt", "w"); f2:write("ammo x3"); f2:close()

_tester('lire("_tmp_a.txt") → "herb"', main.lire("_tmp_a.txt"), "herb")
_tester('lire("_tmp_b.txt") → "ammo x3"', main.lire("_tmp_b.txt"), "ammo x3")

os.remove("_tmp_a.txt")
os.remove("_tmp_b.txt")

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

