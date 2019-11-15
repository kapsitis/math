package lv.ddgatve.math.build

import java.io.File
import org.apache.commons.io.FileUtils
import org.apache.commons.io.filefilter.TrueFileFilter

import scala.collection.JavaConversions._
import scala.collection.mutable.ListBuffer

import sys.process._

object BuildSite {
  
  def copyDirectory(src:String, dest:String): Unit = {
    println("src is " + src)
    println("dest is " + dest)
    //FileUtils.copyDirectory(new File(src), new File(dest))
  }
   
  def rmDirectory(src:String): Unit = {
    FileUtils.deleteDirectory(new File(src))
  }
  
  
  
  
  def main(args:Array[String]): Unit = {
    //println("HEHE")
    
    val resTypes = List("problembase", "numtheory", "algorithms", "visualizations","rbs") // 'discrete', 'datasearch'
    val skip_directories = List("source-material","static","analysis")
   
    // osName - either "Linux" or "Windows 10" (need to know, which computer we are on)
    val osName = System.getProperty("os.name")

    // destRoot:String: relative name for the directory, where to copy transformation results
    val destRoot = if (osName == "Linux") {
      "../../../../workspace-new/linen-tracer-682"
    } else {
       "../../../../workspace/linen-tracer-682"
    }

    for (resType <- resTypes) {
      //println(s"Destination for presentations - $destRoot/$resType-tales")
      val srcRoot = s"../../src/site/$resType"
      val srcRootFile = new File(srcRoot)
      //println("file is " + srcRoot)
  
      val subDirList = srcRootFile.listFiles.filter(_.isDirectory).toList
      val subPresentations = subDirList.filter(p => !skip_directories.contains(p.getName))
      
      //println("# of presentations: " + subPresentations.size)
          
      for (dd <- subPresentations) {
        if (resType == "rbs" && dd.getName() == "youtube-data-part1") {
           println(s"Processing with pandoc/reveal, dir=$dd")
           copyDirectory(dd.getAbsolutePath, destRoot + "/" + resType + "-tales/" + dd.getName)
        }
        
//        val out = Process(Seq(
//            "pandoc","-t","revealjs","-s",
//            "-o","content.html","content.md","--slide-level=2",
//            "-V","revealjs-url=../../reveal.js","--metadata", "pagetitle=\"Uzdevumi\"",
//            "--mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML",
//            "-V", "theme=white"), dd).!!
//        println("out = " + out)
        
      }
    }
  }
}