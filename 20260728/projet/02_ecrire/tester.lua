-- ============================================================
-- Tester — Écrire une sauvegarde
-- ============================================================

-- nettoie avant
os.remove("sauvegarde.txt")

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


local f = io.open("sauvegarde.txt", "r")
local ok_existe = f ~= nil
local texte = ok_existe and f:read("*a") or nil
if f then f:close() end

_tester("sauvegarde.txt existe", ok_existe, true)
_tester('contenu == "vie=80"', texte, "vie=80")

os.remove("sauvegarde.txt")

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

