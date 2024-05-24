from main import Solution


def test_merge_alternately():
    solution = Solution()

    # Test Case 1
    word1 = "abc"
    word2 = "pqr"
    expected_output = "apbqcr"
    assert solution.mergeAlternately(word1, word2) == expected_output, f"Test Case 1 Failed: expected {expected_output}, got {solution.mergeAlternately(word1, word2)}"
    print("Test Case 1 Passed")

    # Test Case 2
    word1 = "ab"
    word2 = "pqrs"
    expected_output = "apbqrs"
    assert solution.mergeAlternately(word1, word2) == expected_output, f"Test Case 2 Failed: expected {expected_output}, got {solution.mergeAlternately(word1, word2)}"
    print("Test Case 2 Passed")

    # Test Case 3
    word1 = "abcd"
    word2 = "pq"
    expected_output = "apbqcd"
    assert solution.mergeAlternately(word1, word2) == expected_output, f"Test Case 3 Failed: expected {expected_output}, got {solution.mergeAlternately(word1, word2)}"
    print("Test Case 3 Passed")


# Run the tests
test_merge_alternately()
