function love.load()
  love.graphics.setBackgroundColor(0.08, 0.08, 0.12)

  paddle = {
    w = 120,
    h = 16,
    x = 0,
    y = 0,
  }
  paddle.x = (love.graphics.getWidth() - paddle.w) / 2
  paddle.y = love.graphics.getHeight() - 40
end

function love.draw()
  love.graphics.setColor(0.9, 0.9, 0.95)
  love.graphics.rectangle("fill", paddle.x, paddle.y, paddle.w, paddle.h, 4, 4)
end
