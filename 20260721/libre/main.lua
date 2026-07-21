-- ============================================================
-- Nahla — Coût de son existence
-- ============================================================
-- Âge ? 4
-- → 4 ans. ~2190€ de croquettes. T'aurais pu t'acheter une PS5.
-- ============================================================
print("Quel age a Nahla ? ")
age = tonumber(io.read())

if age <= 0 then
    print("Nahla n'existe pas")
elseif age <= 4 and age > 0 then
    print("Nahla est toute petite, ELLE EST TROP KAWAI")
elseif age <= 10 and age > 4 then
    print("C'était quand Nahla commencait à devenir grosse")
elseif age <= 15 and age > 10 then
    print("Nahla commence à devenir une racaille")
elseif age > 15 then
    print("Wesh Nahla elle est vieille")
else
    print("?")
end