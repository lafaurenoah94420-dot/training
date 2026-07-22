-- ============================================================
-- Nahla — Buffet de croquettes
-- ============================================================
-- Faim de départ ? 40
-- Nahla mange... faim = 30
-- Nahla mange... faim = 20
-- Nahla mange... faim = 10
-- Nahla mange... faim = 0
-- Nahla est pleine. Elle va dormir sur le clavier.
-- ============================================================
print("Combien de croquettes Nahla a mangé ?")
croquettes = tonumber(io.read())

while croquettes < 50 do
    croquettes = croquettes + 10
    print("Nahla remplit... croquettes = " .. croquettes)
end