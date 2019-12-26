package lv.ddgatve.math.build

import java.io.File
import org.apache.commons.io.FileUtils
import org.apache.commons.io.filefilter.TrueFileFilter

//import scala.collection.JavaConversions._
import scala.collection.mutable.ListBuffer

import sys.process._
import java.io.ByteArrayOutputStream
import java.io.PrintWriter

object MakeReveal {
  
  def runCommand(cmd: Seq[String], dd:File): (Int, String, String) = {
    val stdoutStream = new ByteArrayOutputStream
    val stderrStream = new ByteArrayOutputStream
    val stdoutWriter = new PrintWriter(stdoutStream)
    val stderrWriter = new PrintWriter(stderrStream)
    //val exitValue = cmd.!(ProcessLogger(stdoutWriter.println, stderrWriter.println))
    val exitValue = Process(cmd,dd).!(ProcessLogger(stdoutWriter.println, stderrWriter.println))
    stdoutWriter.close()
    stderrWriter.close()
    (exitValue, stdoutStream.toString, stderrStream.toString)
  }
  
	def main(args: Array[String]): Unit = {
			if (args.length < 1) {
				println("Please specify directory")
			} 
			else {
			  val dd = new File(args(0))
			  val pandocCmd = Seq(
						"/usr/bin/pandoc", "-t", "revealjs", "-s",
						"-o", "content.html", "content.md", "--slide-level=2",
						"-V", "revealjs-url=../../reveal.js", "--metadata", "pagetitle=\"Uzdevumi\"",
						"--mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML",
						"-V", "theme=white")
			  val dummyCmd = Seq("/home/kalvis/workspace/math/samplescript.sh")			  
			  val (exitValue,out,err) = runCommand(dummyCmd,dd)
			  
				println(s"out = $out")
				println(s"err = $err")
				println(s"exitValue = $exitValue")
			}


	}

}