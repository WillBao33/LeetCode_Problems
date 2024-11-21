class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def log_key(log):
            identifier, rest = log.split(" ", 1)

            if rest[0].isalpha():
                return (0, rest, identifier)
            else:
                return (1, )
            
        return sorted(logs, key=log_key)