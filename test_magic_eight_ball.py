import magic_eight_ball
from unittest.mock import patch
import random

def test_magic_eight_ball():
  random.seed(10)
  
  with patch('random.randint', return_value=1):
    result = magic_eight_ball.magic_eight_ball("Alice", "Will it rain today?")
    assert result == "Alice asks: Will it rain today?\nMagic 8-Balls answer: Yes - definitely"
  
  with patch('random.randint', return_value=2):
    result = magic_eight_ball.magic_eight_ball("Bob", "Should I take the job?")
    assert result == "Bob asks: Should I take the job?\nMagic 8-Balls answer: It is decidedly so"

  with patch('random.randint', return_value=3):
    result = magic_eight_ball.magic_eight_ball("Charlie", "What is the meaning of life?")
    assert result == "Charlie asks: What is the meaning of life?\nMagic 8-Balls answer: Without a doubt"

  with patch('random.randint', return_value=4):
    result = magic_eight_ball.magic_eight_ball("David", "Will everthing be alright?")
    assert result == "David asks: Will everthing be alright?\nMagic 8-Balls answer: Reply hazy, try again"

  with patch('random.randint', return_value=5):
    result = magic_eight_ball.magic_eight_ball("Eve", "Will I get the job?")
    assert result == "Eve asks: Will I get the job?\nMagic 8-Balls answer: Ask again later"
  
  with patch('random.randint', return_value=6):
    result = magic_eight_ball.magic_eight_ball("Frank", "Do you think I should do it?")
    assert result == "Frank asks: Do you think I should do it?\nMagic 8-Balls answer: Better not tell you now"

  with patch('random.randint', return_value=7):
    result = magic_eight_ball.magic_eight_ball("George", "What is the meaning of life?")
    assert result == "George asks: What is the meaning of life?\nMagic 8-Balls answer: My sources say no"

  with patch('random.randint', return_value=8):
    result = magic_eight_ball.magic_eight_ball("Henry", "Will it rain tomorrow?")
    assert result == "Henry asks: Will it rain tomorrow?\nMagic 8-Balls answer: Outlook not so good"

  with patch('random.randint', return_value=9):
    result = magic_eight_ball.magic_eight_ball("Ian", "Will I be okay with it?")
    assert result == "Ian asks: Will I be okay with it?\nMagic 8-Balls answer: Very doubtful"

  with patch('random.randint', return_value=10):
    result = magic_eight_ball.magic_eight_ball("Ian", "Will I be okay with it?")
    assert result == "Ian asks: Will I be okay with it?\nMagic 8-Balls answer: Error"
