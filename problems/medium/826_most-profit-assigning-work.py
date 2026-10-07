class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        # Combine jobs into (difficulty, profit) pairs and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        # Sort workers by their ability
        worker.sort()

        total_profit = 0          # final sum of profits
        best_profit = 0           # max profit among jobs that are within current worker's ability
        job_idx = 0               # current position in jobs array
        n = len(jobs)

        # Process each worker in increasing ability order
        for ability in worker:
            # Advance through all jobs that this worker can handle (difficulty <= ability)
            while job_idx < n and jobs[job_idx][0] <= ability:
                # Update best profit we've seen so far
                best_profit = max(best_profit, jobs[job_idx][1])
                job_idx += 1
            # best_profit now holds the maximum profit achievable for this worker
            total_profit += best_profit

        return total_profit