package lv.ddgatve.math.build

import java.io.File
import org.apache.commons.io.FileUtils
import org.apache.commons.io.filefilter.TrueFileFilter

import scala.collection.JavaConversions._
import scala.collection.mutable.ListBuffer

object BuildSite {
  
  def copyDirectory(src:String, dest:String): Unit = {
    FileUtils.copyDirectory(new File(src), new File(dest))
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
    println("osName is " + osName)
    println("DestRoot is " + destRoot)
    
    for (resType <- resTypes) {
      println(s"Destination for presentations - $destRoot/$resType-tales")
      val srcRoot = new File(s"../../src/site/$resType")
      println("file is " + srcRoot)
      val subDirectories = FileUtils.listFilesAndDirs(srcRoot,
          TrueFileFilter.INSTANCE, TrueFileFilter.INSTANCE)
      
      val subDirIter = subDirectories.iterator()
      var subDirList = new ListBuffer[File]()
      while (subDirIter.hasNext()) {
        val ff = subDirIter.next()
        if (ff.isDirectory()) {
          subDirList += ff
          println("ff is " + ff)
        }
      }
      
      println("subDirList is " + subDirList.size)
          
      //for (dd <- subDirectories) {
      //  println(s"Processing with pandoc/reveal, dir=$dd")
      //}
    }
    
  }
  
}