-- ============================================================
-- Tester — Fonction aléatoire
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

if type(main.jet) ~= "function" then
  print("❌ Erreur : la fonction jet n'est pas définie")
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


math.randomseed(42)
local a = main.jet(1, 6)
math.randomseed(42)
local b = main.jet(1, 6)
_tester("jet reproductible avec même graine", a, b)
_tester("jet(1, 6) dans la plage", a >= 1 and a <= 6, true)
math.randomseed(1)
local c = main.jet(10, 10)
_tester("jet(10, 10) → 10", c, 10)


local _passes = 0
for _, r in ipairs(_resultats) do if r then _passes = _passes + 1 end end
local _total = #_resultats
print("\n" .. string.rep("─", 40))
print(string.format("  %d/%d tests passés", _passes, _total))
if _passes == _total then print("  🎉 Parfait !")
else print(string.format("  %d test(s) à corriger.", _total - _passes)) end
print(string.rep("─", 40))
