my $file = "$ARGV[0]";
open IN,$file or die $!;
my $hash = {};my $hash_sort ={};my $count = 1;
while(<IN>){
	my @array = split(/\s+/,$_);
	my $mrna = $array[2];
	my $chr = $array[0];
	my $start = $array[1];
	my $end = $array[1];
	my $strand = $array[3];
	unless (exists $hash->{$mrna}){
		$hash_sort->{$count} = $mrna;$count ++;
		$hash->{$mrna}->{CDS} = "$chr\tensembl\tCDS\t$start\t$end\t.\t$strand\t0\tID=CDS:lzs_made_it;Parent=transcript:$mrna\n";
		$hash->{$mrna}->{mRNA} = "$chr\tensembl\tmRNA\t$start\t";
	}
	else {
		$hash->{$mrna}->{end} = "$end\t.\t$strand\t.\tID=transcript:$mrna\n";
		$hash->{$mrna}->{CDS} .= "$chr\tensembl\tCDS\t$start\t$end\t.\t$strand\t0\tID=CDS:lzs_made_it;Parent=transcript:$mrna\n";
	}
}
for(my $i=1;$i <= $count;$i++){
	my $key = $hash_sort->{$i};
	my $mRNA = $hash->{$key}->{mRNA}.$hash->{$key}->{end};
	my $cds = $hash->{$key}->{CDS};
	print $mRNA;print $cds;
}
	

