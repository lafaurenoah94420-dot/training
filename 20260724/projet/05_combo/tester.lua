-- ============================================================
-- Tester — Défaut + double return
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

if type(main.stats) ~= "function" then
  print("❌ Fonction stats manquante"); os.exit(1)
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


local v, a = main.stats(80)
_tester("stats(80) vie → 80", v, 80)
_tester("stats(80) armure → 0", a, 0)
local v2, a2 = main.stats(50, 25)
_tester("stats(50, 25) vie → 50", v2, 50)
_tester("stats(50, 25) armure → 25", a2, 25)


local _passes = 0
for _, r in ipairs(_resultats) do if r then _passes = _passes + 1 end end
local _total = #_resultats
print("\n" .. string.rep("─", 40))
print(string.format("  %d/%d tests passés", _passes, _total))
if _passes == _total then print("  🎉 Parfait !")
else print(string.format("  %d test(s) à corriger.", _total - _passes)) end
print(string.rep("─", 40))
