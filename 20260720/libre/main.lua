-- ============================================================
-- Nahla — Score de mépris
-- ============================================================
-- Regard (0-10) ? 2
-- → Mépris : élevé. Tu n'existes presque pas.
-- ============================================================
print("A quel point tu regarde Nahla ?")
regard = tonumber(io.read())

if regard <= 0 then
    print("Nahla est... grosse")
elseif regard > 0 and regard <= 4 then
    print("Nahla n'aime pas comment tu la regarde")
elseif regard > 4 and regard <= 9 then
    print("Nahla : 'Comment un esclave de ton genre ause regarder sa reine ?! maintenant va me faire des croquettes'")
elseif regard > 9 then
    print("NE ME REGARDE PAS COMME CA HUMAIN")