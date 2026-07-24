-- ============================================================
-- Tester — Kit joueur
-- ============================================================

local function load_main()
  local env = setmetatable({}, { __index = _G })
  local chunk, err = loadfile("main.lua", "t", env)
  if not chunk then print("❌ " .. tostring(err)); os.exit(1) end
  local ok, err2 = pcall(chunk)
  if not ok then print("❌ " .. tostring(err2)); os.exit(1) end
  return env
end

local main = load_main()

if type(main.creer) ~= "function" then
  print("❌ Fonction creer manquante"); os.exit(1)
end

if type(main.soigner) ~= "function" then
  print("❌ Fonction soigner manquante"); os.exit(1)
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


local j = main.creer("Ellie")
_tester('creer("Ellie").nom → Ellie', j.nom, "Ellie")
_tester("creer armure défaut → 0", j.armure, 0)
local j2 = main.creer("Joel", 50)
_tester("creer avec armure 50", j2.armure, 50)
_tester("soigner(80) → 100", main.soigner(80), 100)
_tester("soigner(80, 5) → 85", main.soigner(80, 5), 85)
_tester("soigner(95, 20) → 100", main.soigner(95, 20), 100)


local _passes = 0
for _, r in ipairs(_resultats) do if r then _passes = _passes + 1 end end
local _total = #_resultats
print("\n" .. string.rep("─", 40))
print(string.format("  %d/%d tests passés", _passes, _total))
if _passes == _total then print("  🎉 Parfait !")
else print(string.format("  %d test(s) à corriger.", _total - _passes)) end
print(string.rep("─", 40))
