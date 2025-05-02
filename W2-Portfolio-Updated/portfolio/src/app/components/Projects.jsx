import React from 'react'
import Image from 'next/image'
import { assets, workData } from '../../../assets/assets'
import { motion } from 'framer-motion'

const Projects = () => {
  return (
    <div id="projects" className='w-full px-[12%] py-10 scroll-mt-20'>
    <motion.div
        initial={{opacity:0, y:100}}
        whileInView={{opacity:1, y:0}}
        transition={{duration: 0.7, type: 'tween'}}>
        <h4 className='text-center mb-2 text-lg Ovo'>My Work</h4>
        <h2 className='text-center text-5xl Ovo'>Projects</h2>

        <p className='text-center max-w-2xl mx-auto mt-5 mb-12 Ovo'>


        Here are a few projects I’ve worked on that show my experience in software development and my interest in AI and machine learning. They’ve been great opportunities to apply my math background, learn new tools, and build things I’m proud of.
        </p>

        <div className='grid lg:grid-cols-4 my-10 gap-6'>
            {workData.map((project, index)=>(<a href={project.link} target='_blank' key={index}>
                <div
                style={{backgroundImage: `url(${project.bgImage})`, backgroundSize: 'cover', backgroundPosition: 'center'}} 
                className='aspect-square bg-no-repeat bg-cover bg-center rounded-lg relative cursor-pointer group'>
                    <div className='bg-white w-10/12 rounded-md absolute bottom-5 left-1/2 -translate-x-1/2 py-3 px-5 flex items-center justify-between duration-500 group-hover:bottom-7'>
                        <div>
                            <h2 className='font-semibold'>{project.title}</h2>
                            <p className='text-sm text-gray-700'>{project.description}</p>
                        </div>
                        <div className='border rounded-full border-black w-9 aspect-square flex items-center justify-center shadow-[2px_2px_0px_#000] group-hover:bg-lime-100 transition'>
                            <Image src={assets.send_icon} alt="" className='w-5'/>
                        </div>
                    </div>
                </div>
            </a>
            ))}
        </div>
        <a href="https://github.com/Daynel-Kem" target="_blank"
            className='w-max flex items-center justify-center gap-2 px-10 py-2 border-[0.5px] border-gray-700 rounded-full y-3 mx-auto my-20 hover:bg-cyan-50 hover:-translate-y-1 duration-500 hover:shadow-2xl'> 
                Show More <Image src={assets.right_arrow_bold} alt="" className='w-4'/>
        </a>
    
    </motion.div>
    </div>
  )
}

export default Projects
