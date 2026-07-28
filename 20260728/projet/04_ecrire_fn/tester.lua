-- ============================================================
-- Tester — Fonction pour écrire
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


if type(main.ecrire) ~= "function" then
  print("❌ Erreur : la fonction ecrire n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function ecrire(...)")
  os.exit(1)
end


main.ecrire("_out_a.txt", "Joel")
main.ecrire("_out_b.txt", "score=12")

local function lire_fichier(path)
  local f = io.open(path, "r")
  if not f then return nil end
  local t = f:read("*a")
  f:close()
  return t
end

_tester('ecrire Joel', lire_fichier("_out_a.txt"), "Joel")
_tester('ecrire score=12', lire_fichier("_out_b.txt"), "score=12")

os.remove("_out_a.txt")
os.remove("_out_b.txt")

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

