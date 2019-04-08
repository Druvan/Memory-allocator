#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>



int main( int argc, char * argv [] ) {
    if(argc != 4){
        printf("Wrong number of arguments, Should be total_ram, mem_percent, time_in_s");
        return 1;
    }
    long long total_ram = atol(argv[1])*1000;
    int mem_percent = atoi(argv[2]);
    int time_in_s = atoi(argv[3]);
    // printf("total_ram: > 0 is %llu, mem_percent: >= 0 is %d, time_in_s: > 0 is %d \n",total_ram,mem_percent,time_in_s);
    if (total_ram > 0 && mem_percent >= 0 && time_in_s > 0){
        long bytes_to_allocate = total_ram*mem_percent*0.01;
        char* ptr = (char*)calloc(bytes_to_allocate,sizeof(char));
        // printf("%zu\n",bytes_to_allocate);
        if(ptr == NULL)                     
        {
            printf("Error! memory not allocated. malloc\n");
            exit(0);
        }
        // int ret_mlock = mlock(ptr,bytes_to_allocate);
        // if(ret_mlock <0){
        //     printf("Error! memory not allocated. mlock\n");
        //     exit(0);
        // }
        char* to_set = "kaUtWcYLNN45U07sBWuuQrisLPWjFTtBZadEk4eVmTOGcE11UYkhSNeOz8WF6hDOFWY9iXMAVqnwZMOAgOj0DCYaq5OqH2IYhlHGGIlElrznyTQR5cabcxiSBJiducr46hXFT8GT7HgzzTEHvNqg9mz2HPVeRRXJxkM6VUYwBcZ5bHMlG9l7PkDfuj2laEEs9RXT11t9VN00mhRj4ObJ8zmBA90i1JQf9MH7DmjAZehKwntHplsUy8kAB0XvTESZYdaakad3VnnvBDARTBUnAH60Syx9GZAvSxacl9yTYuuXuVAwIr5EqyIgswhd9H8BFHYavcQd7Oc8yIcUaXgcyaMu8g4KvMRFW8sAPXn2MDxlJ7ey8oXt45aaRkMaNRWSFcbuO8ASGH4NSO4nuPsesoluNelBsQbkte43PpCIKCKu59D45MM0t6XQhv9LG4xGaqgeDfhHLDsfZX8OBDFfQn1XnmELoagLtMVu39Ui9eGf0C9BjJypdTNZkEwD4iBNwti5Uw34S90NAXWeh9pEaBoxmm1b4Fch342ihtWbDLplOfhPDPqYO36b7Rk3DdqvE7lZDvQbnILQV6zIlicrKiG60lVjHYGQ1l7ANrSupAayU7WROBbWIihgnR6YOSme5SsZXJT2qZHW6JvcTroyl87dEEVn7ycgFMb78DgcgjqTR9blKsSF6H5gdODzibJhMZX8k6RdCdSOskUbmEzqHZuTM75wSW4NOtY5YLXOJMIHWyw3KsdD7yiAU3VcL9tzPGaxEfqWKeGIg6BAwddZ1e8mj4EWYNKb6sJDIwZuUkn8JWeJ8nokLMhmtVMciIPnCBplpmNW9VEX7qpHWzHGB4J31eDs6ZH3wTRoWZlctmNunWBREpMR9JdEIkWXi5eeM7bxdX2P7aMQ5zxwO37N2ijVFU2tlhl3N4jP0TtjnqR6tMoGmIVRAqy6xe3l8uUXT4FmDftOKhD9vxMcX0WQQHlCHREnCWJOuNpCIu76MhJt2V3LZWJGpxjgSUg7YxBD";
        
        // memset(ptr,'x',bytes_to_allocate);
        for(long long i = 0; i < bytes_to_allocate-1024; i += 1024)
        {
            strcpy(&ptr[i], to_set);
            // printf("\ntest! %c\n",ptr[i]);
        }
        sleep(time_in_s);
        // munlock(ptr,bytes_to_allocate);
        free(ptr);
    } else {
        printf("Args needs to be , total_ram: > 0 is %llu, mem_percent: >= 0 is %d, time_in_s: > 0 is %d \n",total_ram,mem_percent,time_in_s);
        return 1;   
    }
}
