#include <stdio.h>
#include "../exemplo/structs.h"

// Teste de comentário 1

/* Teste de comentário 2 */

/* Teste de comentário 3 */ /* Teste de comentário 4 */

// /* Teste de comentário 5 */ /* Teste de comentário 6 */

/*ABCDE
Teste de comentário 6.1
FGHIJ*/

void funcao(int i, int j){
    return i+j;
}

int main(){
    int x = 2; // Teste de comentário 7
    char          * p = "TESTE DE STRING";
    printf("Just a test!, %d\n", /* Teste de comentário 8 */ x);
    printf("/* Teste de comentário INCORRETO 1 */\n", x);
    int r = fun

    return 0; /* Teste de comentário 9 */
}
