-- ============================================================
-- Tester — Copier un fichier
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


if type(main.copier) ~= "function" then
  print("❌ Erreur : la fonction copier n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function copier(...)")
  os.exit(1)
end


local f = io.open("_src.txt", "w"); f:write("munition"); f:close()
main.copier("_src.txt", "_dst.txt")

local g = io.open("_dst.txt", "r")
local dst = g and g:read("*a") or nil
if g then g:close() end

_tester('copie == "munition"', dst, "munition")

-- second test
local f2 = io.open("_src2.txt", "w"); f2:write("clé or"); f2:close()
main.copier("_src2.txt", "_dst2.txt")
local g2 = io.open("_dst2.txt", "r")
local dst2 = g2 and g2:read("*a") or nil
if g2 then g2:close() end
_tester('copie == "clé or"', dst2, "clé or")

os.remove("_src.txt"); os.remove("_dst.txt")
os.remove("_src2.txt"); os.remove("_dst2.txt")

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

