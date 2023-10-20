class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ujemajoce = ""
        strs.sort()
        prva_beseda = strs[0]
        zadnja_beseda = strs[-1]

        krajsa_beseda = min(len(prva_beseda), len(zadnja_beseda)) # iteriramo po crkah krajse besede (da bo manj primerjanj)

        for i in range(krajsa_beseda):
            if prva_beseda[i] != zadnja_beseda[i]: # ce se crki ne ujemata, vrnemo dozdaj najden prefix ( '', ce se ze iz starta ne ujemata)
                return ujemajoce 
            ujemajoce += prva_beseda[i] # ce se ujemata, se crki ujemata, dodamo crko v prefix
        return ujemajoce 
