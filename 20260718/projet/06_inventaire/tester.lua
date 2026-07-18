-- ============================================================
-- Tester — Inventaire complet
-- ============================================================

local function load_main()
  local env = setmetatable({}, { __index = _G })
  local chunk, err = loadfile("main.lua", "t", env)
  if not chunk then
    print("❌ Erreur de chargement : " .. tostring(err))
    print("   → Vérifie que main.lua existe et n'a pas d'erreur de syntaxe")
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

if type(main.creer) ~= "function" then
  print("❌ Erreur : la fonction creer n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function creer(...)")
  os.exit(1)
end

if type(main.ajouter) ~= "function" then
  print("❌ Erreur : la fonction ajouter n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function ajouter(...)")
  os.exit(1)
end

if type(main.taille) ~= "function" then
  print("❌ Erreur : la fonction taille n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function taille(...)")
  os.exit(1)
end

if type(main.contient) ~= "function" then
  print("❌ Erreur : la fonction contient n'est pas définie dans main.lua")
  print("   → Vérifie que tu as bien écrit : function contient(...)")
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

-- ---- Tests ----

local inv = main.creer()
_tester("creer() → table vide", #inv, 0)
main.ajouter(inv, "bandage")
main.ajouter(inv, "eau")
_tester("taille après 2 ajouts → 2", main.taille(inv), 2)
_tester('contient(inv, "eau") → true', main.contient(inv, "eau"), true)
_tester('contient(inv, "fusil") → false', main.contient(inv, "fusil"), false)
local vide = main.creer()
_tester("contient(vide, \"x\") → false", main.contient(vide, "x"), false)


-- ---- Résultat ----
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
