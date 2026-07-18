-- ============================================================
-- Nahla — Mode du moment
-- ============================================================
-- Heure ? 14
-- → Nahla dort. Reviens dans 6h pour le prochain repas.
-- ============================================================
print("Il est quelle heure zebi ?")
heure = tonumber(io.read())

if heure <= 8 then
    print("Nahla dort comme un gros caca.")
  elseif heure <= 16 and heure > 8 then
    print("Nahla fait sa life")
  elseif heure <= 24 and heure > 16 then
    print("Nahla réclame son paté avant d'aller dormir")
  else
    print("?")
  end


