#include <stdio.h>
#include <stdlib.h>
#define MAX 10

// Alunos:
// Rossicler Junior
// Lucas Gomes

int *recebe_notas(float*);
void conta_notas(int*, int*, int*);
int percAprov(int*, int*);

int main() {
    int i, *apr, contAprov0=0, contReprov=0, *percAprov, *percReprov, metadeAprov=0;
    float *notas;
    notas = (float *) calloc(MAX, sizeof(float));

    for(i=0; i<MAX; i++){
        printf("Digite o valor %d do vetor: ", i);
        scanf("%f", notas+i);
    }

    printf("\n \n");

    apr = recebe_notas(notas);
    conta_notas(apr, &contAprov, &contReprov);
    percent_aprov(&metadeAprov, &contAprov, &contReprov);

    for(i=0; i<MAX; i++){
        if(*(apr+i) == 1){
            printf("O aluno %d esta aprovado! \n", i);
        }
        else
            printf("O aluno %d esta reprovado! \n", i);
    }

    printf("\nQuantidade de alunos aprovados: %d \n", contAprov);
    printf("Quantidade de alunos reprovados: %d \n", contReprov);
    printf("Porcentagem de alunos aprovados: %d \n", percAprov);
    printf("Porcentagem de alunos reprovados: %d \n", percReprov);

    if(metadeAprov==1){
      printf("Mais da metade da turma aprovada: Sim\n");
    }
    else {
      printf("Mais da metade da turma aprovada: Não\n");
    }

    return 0;
}

int *recebe_notas(float* notas){
    int *apr;
    apr = (int *) calloc(MAX, sizeof(int));

    if(apr == NULL){
        printf("Alocacao falhou! \n");
        exit(1);
    }

    for(int i=0; i<MAX; i++){
        if(*(notas+i) >= 6.0){
            *(apr+i) = 1;
        }
    }

    return apr;
}

void conta_notas(int* apr, int* contAprov, int* contReprov){
    for(int i=0; i<MAX; i++){
        if(*(apr+i) == 1)
            *contAprov += 1;
        else
            *contReprov += 1;
    }
}

int percent_aprov(int* metadeAprov, int* contAprov, int* contReprov){
  *percAprov = (contAprov/MAX)*100;
  *percReprov = (contReprov/MAX)*100;

  if(*percAprov > (MAX/2)){
    metadeAprov = 1;
  }

  return metadeAprov;
}
