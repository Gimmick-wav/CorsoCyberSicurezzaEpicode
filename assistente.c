#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

void normalize_input(char *input)
{
    for (int i = 0; input[i]; i++)
    {
        input[i] = tolower((unsigned char)input[i]);
    }
    size_t len = strlen(input);
    if (len > 0 && input[len - 1] == '\n')
    {
        input[len - 1] = '\0';
    }
}

int main()
{
    char comando[100];
    while (1)
    {
        printf("Cosa vuoi sapere?\n");
        fgets(comando, 100, stdin);
        normalize_input(comando);
        printf(comando);

        if (strcmp(comando, "qual è la data di oggi?") == 0)
        {
            time_t t;
            struct tm *time_info;
            time(&t);
            time_info = localtime(&t);
            // char data_form[50];
        }
        else if (strcmp(comando, "come ti chiami?") == 0)
        {
            printf("\nMi chiamo cAssistente cVirtuale\n");
        }
        else if (strcmp(comando, "esci") == 0)
        {
            printf("\nArrivederci!\n");
            break;
        }
        else
        {
            printf("\nNon ho capito la tua domanda.\n");
        }
    }
    return 0;
}