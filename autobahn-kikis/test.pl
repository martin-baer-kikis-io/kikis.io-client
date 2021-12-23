#!/usr/bin/perl
#-------------------------------------------------------------------------------

=head1 ariba_test.pl

=cut

=head1 Synopsis

    This is an application written as a perl test for an Ariba 
    job application.

    The usage statement is displayed with no arguments as well as 
    with the --help flag as an argument.


    Usage: ./ariba_test.pl {OPTIONS}

        OPTIONS:

            1 - historgram test
                This is implemented as a parse of the input string.
                The string is parsed into a hash reference which holds
                each letter as a key, and the number of occurances as
                the value.
            2 - hash exercise
                This is implemented as a hash reference where first and
                last names are key and value, then sorting and printing 
                is performed using various builtin and coded strategies.
            3 - bracket balanancing
                This is iimplemented as a exercise in recurssion using a
                an array and a base case for each pairing.  Non-fatal
                errors are printed out.
            4 - bracket balancing redux
                This is iimplemented as a single regex testing for each
                permutation of parens.


       COMMANDLINE EXAMPLES:

         ./ariba_test.pl -q 1 -s "Mississippi borders Tennessee."
         ./ariba_test.pl -q 2
         ./ariba_test.pl -q 3 -s "](){"
         ./ariba_test.pl -q 4 -s "()()"

=cut

#-------------------------------------------------------------------------------

=head3 File History

    Sun Oct  2 16:35:16 PDT 2016 - MB - implemented test requirements

=cut

#-------------------------------------------------------------------------------

# these are the only globals PLEASE!
 
our $true  = ( 1 == 1 );
our $false = ( 1 == 0 );


#-------------------------------------------------------------------------------

=head3 Module Dependencies

    use strict;
    use warnings;
    use Getopt::Long;
    use Ariba;

=cut

#-------------------------------------------------------------------------------

# loader section

use strict;
use warnings;
use Getopt::Long;
#use Ariba;

#-------------------------------------------------------------------------------

=head1 Subroutines

    The list of subroutines for this file

=cut

#-------------------------------------------------------------------------------

=head3 print_usage($;)

    This prints the usage message and an optional error message  and exits;

    Example:

        print_usage($msg);

=cut

#-------------------------------------------------------------------------------

sub print_usage (;$) {

    my $msg = shift;

    # POP note; $usage_str is a simple intuitive way to print
    # formatted multi-line messages

    my $usage_str = "

    Usage: ./ariba_test.pl {OPTIONS}

        OPTIONS:

            1 - historgram test
                This is implemented as a parse of the input string.
                The string is parsed into a hash reference which holds
                each letter as a key, and the number of occurances as
                the value.
            2 - hash exercise
                This is implemented as a hash reference where first and
                last names are key and value, then sorting and printing 
                is performed using various builtin and coded strategies.
            3 - bracket balanancing
                This is iimplemented as three  regex testing for each
                of the valid brackets
            4 - bracket balancing part deux
                This is iimplemented as a single regex testing for each
                permutation of parens.
                

       COMMANDLINE EXAMPLES:

         ./ariba_test.pl -q 1 -s \"Mississippi borders Tennessee.\"
         ./ariba_test.pl -q 2
         ./ariba_test.pl -q 3 -s \"](){\"
         ./ariba_test.pl -q 4 -s \"(())\"

    ";

    # append optional msg argument to end of usage message
    # best if message is last string printed to screen

    # add more help?

    $usage_str .= $msg if defined $msg;

    print "$usage_str\n\n";

    exit $false;
}

#-------------------------------------------------------------------------------

=head3 parse_commandline_arguments($;)

    This routine parses the arguments to the application from the commandline.
    It should be the first subroutine called from MAIN.

    Usage:

        $args_href = parse_commandline_arguments ($args_href);

=cut

#-------------------------------------------------------------------------------

sub parse_commandline_arguments ($;) {

    my $args_href = shift;
    my $arg_cnt = @ARGV;
    $args_href->{'arg_cnt'} = $arg_cnt;

    # if no arguments ...?
    if ( $arg_cnt == 0 ) {
        print_usage ( "FATAL: Arguments are required" );
    }

    Getopt::Long::Configure("bundling");
    print "\n";

    my $result = GetOptions(

        "q=s"   => \$args_href->{'q_arg'},
        "s=s"   => \$args_href->{'s_arg'},
        "help"  => \$args_href->{'help_arg'},
    );

    # check for Getopt errors - $result is 1 on success
    if ( $result != 1 ) {
        print_usage ( "FATAL: argument error (see above)" );
    }

    # help argument
    print_usage() if $args_href->{'help_arg'};

    #
    # test argument constraints
    #
    my $question = $args_href->{'q_arg'};
    if ( $question eq "1") {
        print_usage( "FATAL: missing '-s' argument" )
            if ! $args_href->{'s_arg'};
    }
    if ( $question eq "2") {
        print_usage( "WARNING: '-s' argument not required" )
            if $args_href->{'s_arg'};
    }
    if ( $question eq "3") {
        print_usage( "FATAL: missing '-s' argument" )
            if ! $args_href->{'s_arg'};
    }
    if ( $question eq "4") {
        print_usage( "FATAL: missing '-s' argument" )
            if ! $args_href->{'s_arg'};
    }

    return $args_href;
}

#-------------------------------------------------------------------------------

=head3 MAIN()

    The main entry point to the application.

=cut

#-------------------------------------------------------------------------------

{    # MAIN main Main block

    # declare some reusable working variable names
    my ( $args_href, $href, $aref, $msg, $status );

    # parse arguments
    #$args_href = parse_commandline_arguments($args_href);



   # run tests

   my $i;
   while ( $i < 10000 ) {
      system( "make start" );
      sleep (0.25);
      $i++;
      print ("loop $i w/ delay\n");
  }

   exit(0);

   my $question = $args_href->{'q_arg'};

   # test 1
   if ( $question eq "1" ) {

        $status = ariba_test_1 ( $args_href );
   }
   # test 2
   if ( $question eq "2" ) {

        $status = ariba_test_2 ();
   }
   # test 3
   if ( $question eq "3" ) {
        
        $status = ariba_test_3 ( $args_href );
   }
   # test 4
   if ( $question eq "4" ) {

        $status = ariba_test_4 ( $args_href );
   }

    exit 0; # success 
}

#-------------------------------------------------------------------------------

=head1 ^

=cut

# EOF
