func maxTaskAssign(tasks []int, workers []int, pills int, strength int) int {
    task_requirements := append([]int(nil), tasks...)
    worker_strengths := append([]int(nil), workers...)
    total_pills := pills
    pill_boost := strength
    sort.Ints(task_requirements)
    sort.Ints(worker_strengths)

    can_assign := func(k int) bool {
        avail := append([]int(nil), worker_strengths[len(worker_strengths)-k:]...)
        pills_remain := total_pills
        for i := k - 1; i >= 0; i-- {
            req := task_requirements[i]
            n := len(avail)
            if n > 0 && avail[n-1] >= req {
                avail = avail[:n-1]
            } else {
                if pills_remain <= 0 {
                    return false
                }
                threshold := req - pill_boost
                idx := sort.Search(len(avail), func(j int) bool { return avail[j] >= threshold })
                if idx == len(avail) {
                    return false
                }
                avail = append(avail[:idx], avail[idx+1:]...)
                pills_remain--
            }
        }
        return true
    }

    low, high, completed := 0, min(len(tasks), len(workers)), 0
    for low <= high {
        mid := (low + high) / 2
        if can_assign(mid) {
            completed = mid
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return completed
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}