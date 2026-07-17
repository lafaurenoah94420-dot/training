-- ============================================================
-- Nahla — Verdict croquettes
-- ============================================================
-- Bols mangés ? 3
-- → Verdict : gloutonne. Le canapé tremble.
-- ============================================================
print("combien de bols le gros chat a mangé ?")
question = tonumber(io.read())

function gros_ventre()
    if question == 0 then
        print("Nahla a mangé " .. question .. " bol")
        print("Nahla va crever si elle ne mange pas")
    elseif question > 0 and question < 4 then
        print("Nahla a mangé " .. question .. " bols")
        print("Nahla a mangé régulièrement, son ventre est stable")
    elseif question >= 4 and question < 7 then
        print("Nahla a mangé " .. question .. " bols")
        print("Nahla a beaucoup mangé, son ventre risque d'exploser")
    elseif question >= 7 then
        print("Nahla a mangé " .. question .. " bols")
        print("Nahla est devenue une bombe nucléaire")
    end
end
gros_ventre()