#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

__attribute__((constructor)) void ignore_me() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void print_logo() {
		printf ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXK0kxdolcccclllllcclldxkO0KXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMWNXK0kxdolccccllllccc::;:::::cclllllllllodxkOKXNWWMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMWWNK0Oxdolc:::ccccccc::;,'...          ...',;::cclllllllloodkO0KXNWWMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMWX0Okdolc:::::cccc::::;,....                           ...';::cccllllllllodxkO0KNWMMMMMMMMM\n",
"MMMMMMMXx:;;;:::cc::::;,'...........       .                            ...',;::cclllllllloONMMMMMMM\n",
"MMMMMMNo.;c::;;,'......................        .,,..                             ...',;:coc:kWMMMMMM\n",
"MMMMMMK:.lc.  ..............................  .cK0x:.                                   .ld;dNMMMMMM\n",
"MMMMMMX:.lc.    ..........c;..............',;:oKMMWKo;;,..             .:;.             .ld;dNMMMMMM\n",
"MMMMMMXc.cc.      .......oXKc.............l0NWMMMMMMMWNOc.            .oXK:.            .lo;xNMMMMMM\n",
"MMMMMMNl.cl.       .;:clkNMMKdlc:,.........;xNMMMMMMMXx,.        .,:clxNMMKdc:;'.       .oo;xWMMMMMM\n",
"MMMMMMNo.:l.       .lKWMMMMMMMMNOc..........;KMMMMMMM0,  .  ..  ..lKWMMMMMMMMNO:.       'oo:kWMMMMMM\n",
"MMMMMMWd.;l'        .'dNMMMMMMKo'...........lXKkoodkKKc. .   .    .,xNMMMMMMKl..        ,dl:OMMMMMMM\n",
"MMMMMMMk.'l,          :XMMWWMMO,............,:'.....';,. ...       .:XMMWWMMO'          ;dcc0MMMMMMM\n",
"MMMMMMM0,.l:         .oKOoccd00c.............................      .oKOoccx00:.        .cd:oXMMMMMMM\n",
"MMMMMMMX:.cc.        .''.   ..,'.................................  .''..  ..,..        .lo;xNMMMMMMM\n",
"dddddddo,.;l.                   ......................................                 'dl;okkkkkkkk\n",
"..;:;;;;;;ld;..........................................................................:kdoooooool:;\n",
".,xkxxxxxxxdl::::::::::::::::::::::cccccccccccc:cc::cc:::::cc:c::::::::::::::::::::::::oxxxxxxxxOOc:\n",
"..dxooooooooooooooooooooooooooooooooooooooloooooooooloooooooooooooooooooooooooooooooloooooooooookx:l\n",
":.lkoooooxOxoxOxkOOOkdooxOOOkkOxoxOxxOOOOkdkOOOkxkOOOOOdoodkOOOkdoxOOdodkOxodkOxxkOOOkxOOOOxooodkd;d\n",
"d.,xxlood0NkxKX0XWNKOdokXXOkxkKXKX0k0WNXWK0NNXXOONWXKXWOodKN0O0OdkXNN0d0NW0kKWW00WNXKO0WNX0xoooxkccO\n",
"K;.lkoooxKN00N0k0XNW0ooONKOkdoONNkoxXWXNWKKWNXKOKNXKXNKxoxXNO0X0OXXKNXOXXKXXKNX0XWXX0kOKNWXxoodkd:dX\n",
"Wx.'dxoooxOOOkdkOOOOxoodkOOkdodkxoodkOOOOxkOOOkxkkxdxOxoooxOOOkxkkddkOkOkxkkxkkxkOOOkxOOOOkdookkcc0W\n",
"MXl.;xxooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooloooooooolooooloxkl:kWM\n",
"MMK:.:xxddddddddolcccccccccccccccccccccccccccccccccccccccccccccccccccccccclccccclcloddddddddkko:xNMM\n",
"MMMKc.,cccccccclo;................................................................:xdooooooooc:xXMMM\n",
"MMMMXdllccllcc,.;l'    ..'.''......''.  ..'..'..'''.''.'..'..'.  ..,,....'..     ,oc;cddddddddONMMMM\n",
"MMMMMMMMMMMMMWK:.:l.    ,:'cl,;c,,;ll,...;c,;l;:oll;::,c;':,;l'...,oo,,;:o:..   'ol,oXMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMW0;.cc.   ................ ............ ........... ...........  'ol,lXMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMWO;.:l:;;;;::;........;:::::::,........,:::::::;'......';:::;:;coc,lKMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMW0;.:OXXNWWWXo,,,,,,lKWWWWWWWk;,,,,,,:kWWWWWWWKo:ccccckNWWWWWN0c,lXMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMKc.;ONWWMMXo,;,,,,oXMMMMMMWk:,,,,,,:OWMMMMMMKl;;:ccckWMMMWNO:,dXMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMXo.'dXWWMXo,,,,,,oXMMMMMMWk:,,,,,,:OWMMMMMMKl,,;;:ckNMMWNx,;xNMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMNk,.c0WWXo;,,,,,oXMMMMMMWk:,,,,,,:OMMMMMMMKl,,,;;:xNMW0l':OWMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMWKc.,xXXo,,,,,,oXMMMMMMWk:,,,,,,:OWMMMMMMKl,,;,,;dNXx;,oXMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMNk;.:xd:,,,,,oXMMMMMMWk:,,,,,,:OWMMMMMMKl,,,,;:xx:':OWMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMXd,.:ol:;,,oXMMMMMMWk:,,,,,,:OWMMMMMMKl,,;:oo:';xXMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMMWKo'.:oo:;oXMMMMMMWk:,,,,,,:OWMMMMMMKl;col:';dXWMMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd,.;loxXMMMMMMWk:,,,;,,:OWMMMMMMXxol;.;xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXx:''ckXWWWMMWk:,,,,,,:OWMWWWWXxc''ckNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0o;',lkKNWNk;,,,,,,:OWWNKxc,';d0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNOo:'':okxoc::::coxko:'':d0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0xl;',;::::::,',;lkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOo;......;oONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n"
	);
	

printf("------------------------------------------------------------------------------------------------------\n");
printf("~ US Cyber Games Team Motto Suggestion Engine v313.37\n");
printf("------------------------------------------------------------------------------------------------------\n");
}

void vuln() {
  void* heap = sbrk(0);
   print_logo();
for (int i=0; i<4; i++) {
   printf("Team size >>> ");
   long unsigned size;
   scanf("%lu",&size);
   char *p = malloc(size);
   char *c;
   c = p;
   printf("Team motto >>> ");
   char data[100];
   scanf("%100s",data);
   strcpy(c, data);
   heap = p;
   printf("<<< Thank you for your suggestion");
   printf("<<< Team data stored securely at : %p\n", heap);
   printf("<<< Random identifier for motto : %p\n", &rand);
 }
}

int main() {
  vuln();
}
