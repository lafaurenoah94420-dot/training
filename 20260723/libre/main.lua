-- ============================================================
-- Nahla — Compte à rebours canapé
-- ============================================================
-- Minutes ? 3
-- ... 2
-- ... 1
-- ... 0
-- → REPAS. Nahla miaule.
-- ============================================================
print("Combien de minutes ?")
minutes = tonumber(io.read())

while minutes > 0 do
    minutes = minutes - 1
    print("minutes restantes avant le repas : " .. minutes)
end
print("REPAS. Nahla miaule.")