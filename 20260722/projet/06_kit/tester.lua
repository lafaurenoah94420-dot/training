-- ============================================================
-- Tester — Kit de combat
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

if type(main.soigner) ~= "function" then
  print("❌ Erreur : la fonction soigner n'est pas définie")
  os.exit(1)
end

if type(main.degats) ~= "function" then
  print("❌ Erreur : la fonction degats n'est pas définie")
  os.exit(1)
end

if type(main.critique) ~= "function" then
  print("❌ Erreur : la fonction critique n'est pas définie")
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


_tester("soigner(90, 20) → 100", main.soigner(90, 20), 100)
_tester("soigner(40, 10) → 50", main.soigner(40, 10), 50)
_tester("degats(30, 50) → 0", main.degats(30, 50), 0)
_tester("degats(80, 15) → 65", main.degats(80, 15), 65)
math.randomseed(42)
local c1 = main.critique(10, 20)
math.randomseed(42)
local c2 = main.critique(10, 20)
_tester("critique reproductible", c1, c2)
_tester("critique dans [10,20]", c1 >= 10 and c1 <= 20, true)


local _passes = 0
for _, r in ipairs(_resultats) do if r then _passes = _passes + 1 end end
local _total = #_resultats
print("\n" .. string.rep("─", 40))
print(string.format("  %d/%d tests passés", _passes, _total))
if _passes == _total then print("  🎉 Parfait !")
else print(string.format("  %d test(s) à corriger.", _total - _passes)) end
print(string.rep("─", 40))
