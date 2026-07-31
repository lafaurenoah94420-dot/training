-- ============================================================
-- The Last of Us — score
-- ============================================================
-- Joel a un dictionnaire de stats. Tu lis son score.
--
-- Lance : lua 02_score.lua
-- ============================================================

stats = { score = 1200, morts = 3 }
score_joel = nil

-- Mets stats.score dans score_joel.
--
-- Résultat attendu : score_joel == 1200
--
-- Indice : stats.score

-- À toi :
score_joel = stats.score

-- --- Vérification (ne pas modifier) ---
assert(score_joel == 1200, "Obtenu : " .. tostring(score_joel))
print("✅ Correct !")
