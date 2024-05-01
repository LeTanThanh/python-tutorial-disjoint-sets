if __name__ == "__main__":
  # Introduction to Python disjoint sets

  """
  set_a.isdisjoint(set_b)
  """

  # Python isdisjoint() method examples

  odd_numbers = {1, 3, 5}
  even_numbers = {2, 4, 6}

  print(odd_numbers)
  print(even_numbers)
  print(odd_numbers.isdisjoint(even_numbers))

  letters = {"A", "B", "C"}
  alphanumerics = {"A", 1, 2}

  print(letters)
  print(alphanumerics)
  print(letters.isdisjoint(alphanumerics))
  print(letters.isdisjoint(["A", 1, 2]))
