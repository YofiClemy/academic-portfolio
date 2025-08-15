// Example Verilog testbench stub
module tb();
  reg clk=0, rst=1;
  always #5 clk = ~clk;
  initial begin
    #20 rst = 0;
    #200 $finish;
  end
endmodule
