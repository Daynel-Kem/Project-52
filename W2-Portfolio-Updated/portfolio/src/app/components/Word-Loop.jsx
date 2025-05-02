"use client"
import * as React from "react"
import { AnimatePresence, motion } from "framer-motion"
 
export function RotateWords({
  text = "Rotate",
  words = ["Word 1", "Word 2", "Word 3"],
}) {
  const [index, setIndex] = React.useState(0)
 
React.useEffect(() => {
const interval = setInterval(() => {
setIndex((prevIndex) => (prevIndex + 1) % words.length)
}, 5000)
// Clean up interval on unmount
return () => clearInterval(interval)
}, [])
return (
 
<div className="text-7xl text-left Ovo">
  {text}{' '}
  <AnimatePresence mode="wait">
    <motion.h3
      key={words[index]}
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: 20 }}
      transition={{ duration: 0.6, type: "spring", bounce: 0.4 }}
      className={`Ovo sm:text-6xl lg:text-[90px] text-center sm:text-left
                ${index==0 ? "text-amber-400" : ""} 
                ${index==1 ? " text-green-300" : ""}
                ${index==2 ? "text-red-800" : ""}`}
    >
      {words[index]}
    </motion.h3>
  </AnimatePresence>
</div>
) }