
func pushDominoes(dominoes string) string {
	arL := make([]int, 0)
	arr := make([]int, 0)
	bt := []byte(dominoes)
	for i := 0; i < len(dominoes); i++ {
		if dominoes[i] == 'L' && (i-1 >= 0 && dominoes[i-1] == '.') {
			arL = append(arL, i)
		}
		if dominoes[i] == 'R' && (i+1 < len(dominoes) && dominoes[i+1] == '.') {
			arr = append(arr, i)
		}
	}
    //BFS
	for len(arL)+len(arr) > 0 {
		arLN := make([]int, 0)
		for _, i := range arL {
			if bt[i-1] == '.' && (i-1 == 0 || bt[i-2] != 'R') {
				if i-1 > 0 {
					arLN = append(arLN, i-1)
				} else {
					bt[i-1] = 'L'
				}
			}
		}
		arrN := make([]int, 0)
		for _, i := range arr {
			if bt[i+1] == '.' && (i+1 == len(dominoes)-1 || bt[i+2] != 'L') {
				if i+1 < len(dominoes)-1 {
					arrN = append(arrN, i+1)
				} else {
					bt[i+1] = 'R'
				}
			}
		}
		for _, i := range arLN {
			bt[i] = 'L'
		}
		for _, i := range arrN {
			bt[i] = 'R'
		}
		arL = arLN
		arr = arrN
	}
	return string(bt)
}