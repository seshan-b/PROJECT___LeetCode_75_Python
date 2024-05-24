class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # 1. Initialize an empty list 'merged'
        # 2. Initialize pointer i and j to 0
        # 3. While i < len(word1) and j < len(word2):
        #     a. Add word1[i] to merged
        #     b. Increment i
        #     c. Add word2[j] to merged
        #     d. Increment j
        # 4. If there are remaining characters in word1 (i < len(word1)):
        #     a. Append the remaining characters to merged
        # 5. If there are remaining characters in word2 (j < len(word2)):
        #     a. Append the remaining characters to merged
        # 6. Join the merged list into a string
        # 7. Return the joined string

        # Step 1: Initialize an empty list 'merged'
        merged = []

        # Step 2: Initialize pointer i and j to 0
        i, j = 0, 0

        # Step 3: Loop through both words until both pointers reach the end of their respective words
        while i < len(word1) and j < len(word2):
            # Step 3a: Add word1[i] to merged
            merged.append(word1[i])
            # Step 3b: Increment i
            i += 1
            # Step 3c: Add word2[j] to merged
            merged.append(word2[j])
            # Step 3d: Increment j
            j += 1

        # Step 4: If there are remaining characters in word1
        if i < len(word1):
            # Step 4a: Append the remaining characters to merged
            merged.extend(word1[i:])

        # Step 5: If there are remaining characters in word2
        if j < len(word2):
            # Step 5a: Append the remaining characters to merged
            merged.extend(word2[j:])

        # Step 6: Join the merged list into a string
        merged_string = ''.join(merged)

        # Step 7: Return the joined string
        return merged_string
